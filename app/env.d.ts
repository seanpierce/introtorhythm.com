/// <reference types="vite/client" />
interface ImportMetaEnv {
    VUE_APP_API_BASE_URL: string;
    // add other VUE_APP_* variables here
  }
  
  declare namespace NodeJS {
    interface ProcessEnv extends ImportMetaEnv {}
  }
  
  declare var process: {
    env: NodeJS.ProcessEnv;
  };