import configparser

class ApiHelper:
    """
    Helper class for API processes.
    """

    @staticmethod
    def verify_header_secret(secret:str, header:str, request) -> bool:
        """
        Method used to verify supplied header secrets against configured variables.
        """
        config = configparser.RawConfigParser()
        config.read('./env.ini')
        config_secret = config.get('Secrets', secret)
        header_secret = request.request.headers[header]
        return config_secret == header_secret