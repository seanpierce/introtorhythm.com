import { defineStore } from 'pinia';
import { ref } from 'vue';
import { io, Socket } from 'socket.io-client';
import { SocketConfig as sock, type ChatMessage } from '@/types';

export const useChatStore = defineStore('chat', () => {
  const messages = ref<ChatMessage[]>([]);
  const messageInput = ref('');
  const usernameInput = ref('');
  const username = ref<string | null>(null);
  const usernameError = ref<string | null>(null);
  let socket: Socket | null = null;

  const connect = (name: string) => {
    console.log('Connecting with username:', name);

    // Socket.IO reconnects this socket automatically. Reusing it avoids creating
    // a second connection if this method is called again while the view remounts.
    if (socket) {
      if (username.value === name && (socket.connected || socket.active)) return;
      socket.disconnect();
    }

    const socketUrl = import.meta.env.VITE_SOCKET_URL;
    socket = io(socketUrl, { transports: ['websocket', 'polling'] });

    socket.on(sock.CONNECT, () => {
      console.log('Socket connected');
      socket?.emit(sock.JOIN, name);
    });

    socket.on(sock.JOIN_SUCCESS, (uname: string) => {
      console.log('Join successful with username:', uname);
      username.value = uname;
      usernameError.value = null;
      localStorage.setItem(sock.GET_LOCAL_USERNAME, uname);
    });

    socket.on(sock.JOIN_ERROR, (err: string) => {
      console.error('Join error:', err);
      usernameError.value = err;
      username.value = null;
      socket?.disconnect();
    });

    socket.on(sock.CHAT_MESSAGES, (msgs: ChatMessage[]) => {
      // Filter out duplicates
      const messagesToPush = msgs.filter(
        (m) => !messages.value.find((existing) => existing.id === m.id),
      );
      messages.value.push(...messagesToPush);
    });
  };

  const resetUsernameError = () => {
    usernameError.value = null;
  }

  const sendMessage = () => {
    if (!messageInput.value.trim() || !socket || !username.value) return;
    socket.emit(sock.CHAT_MESSAGE, username.value, messageInput.value);
    messageInput.value = '';
  };

  const setUsername = () => {
    const trimmed = usernameInput.value.trim();
    console.log('Attempting to set username:', trimmed);
    if (!trimmed) return;
    connect(trimmed);
    usernameInput.value = '';
  };

  const unsetUsername = () => {
    if (!socket || !username.value) return;
    username.value = null;
    localStorage.removeItem(sock.GET_LOCAL_USERNAME);

    const loggingOutSocket = socket;
    socket = null;

    // Wait for the server to record the explicit logout before closing. The
    // timeout still guarantees local cleanup if the connection has already died.
    loggingOutSocket.timeout(2000).emit(sock.LOGOUT, () => {
      loggingOutSocket.disconnect();
    });
  };

  const getUsernameFromLocalStorage = () => {
    const username = localStorage.getItem(sock.GET_LOCAL_USERNAME);
    if (username) {
      connect(username);
    }
  };

  return {
    messages,
    messageInput,
    usernameInput,
    username,
    usernameError,
    connect,
    sendMessage,
    setUsername,
    unsetUsername,
    getUsernameFromLocalStorage,
    resetUsernameError,
  };
});
