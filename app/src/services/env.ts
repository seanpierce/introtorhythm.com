function getEnvVar(key: string, defaultValue?: string): string {
    const value = process.env[key];
  
    if (value !== undefined) {
      return value;
    }
  
    if (defaultValue !== undefined) {
      return defaultValue;
    }
  
    throw new Error(`Environment variable ${key} is required but was not provided.`);
  }
  
  export const ENV = {
    ApiBaseUrl: getEnvVar('VUE_APP_API_BASE_URL')
  };