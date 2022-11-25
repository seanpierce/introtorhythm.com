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


    @staticmethod
    def get_date_string_from_filename(filename:str) -> str:
        """
        ex: ITR_rec_20221123-090448.mp3
        """

        output = filename.replace('ITR_rec_', '')
        output = output.split('-')[0]
        output = f"{output[:4]}-{output[4:6]}-{output[6:]}"
        return output


    @staticmethod
    def get_hour_from_filename(filename:str) -> int:
        """
        ex: ITR_rec_20221123-090448.mp3
        """

        output = filename.replace('ITR_rec_', '')
        output = output.split('-')

        hour = int(output[1][:2])
        minutes = int(output[1][2:4])

        # set threshold for rounding up if
        # the stream started slightly before the hour
        if minutes > 50:
            hour = hour + 1

        return hour