import { ENV } from "@/services/env";

const BASE_URL = `${ENV.ApiBaseUrl}/api/`; 

type HttpMethod = 'GET' | 'POST' | 'PUT' | 'DELETE' | 'PATCH';

interface IRequestOptions<T = unknown> {
  method?: HttpMethod;
  data?: T;
  headers?: HeadersInit;
  params?: Record<string, string | number | boolean>;
}

const request = async <TResponse = unknown, TBody = unknown>(
  endpoint: string,
  options: IRequestOptions<TBody> = {}
): Promise<TResponse> => {
  const { method = 'GET', data, headers = {}, params = {} } = options;

  const queryString = new URLSearchParams(
    Object.entries(params).reduce((acc, [key, val]) => {
      acc[key] = String(val);
      return acc;
    }, {} as Record<string, string>)
  ).toString();

  const url = `${BASE_URL}${endpoint}${queryString ? `?${queryString}` : ''}`;

  const config: RequestInit = {
    method,
    headers: {
      'Content-Type': 'application/json',
      ...headers,
    },
    ...(data && method !== 'GET' ? { body: JSON.stringify(data) } : {}),
  };

  const response = await fetch(url, config);
  if (!response.ok) {
    const errorData = await response.json().catch(() => ({}));
    throw new Error(errorData.message || `Request failed: ${response.status}`);
  }
  return await (response.json() as Promise<TResponse>);
};

/**
 * Simple API Client implementation using the native Fetch API.
 */
export const apiClient = {
  getAsync: <T = unknown>(url: string, options?: IRequestOptions): Promise<T> =>
    request<T>(url, { ...options, method: 'GET' }),

  postAsync: <T = unknown, B = unknown>(url: string, data: B, options?: IRequestOptions): Promise<T> =>
    request<T, B>(url, { ...options, method: 'POST', data }),

  putAsync: <T = unknown, B = unknown>(url: string, data: B, options?: IRequestOptions): Promise<T> =>
    request<T, B>(url, { ...options, method: 'PUT', data }),

  deleteAsync: <T = unknown>(url: string, options?: IRequestOptions): Promise<T> =>
    request<T>(url, { ...options, method: 'DELETE' }),
};

export default apiClient;