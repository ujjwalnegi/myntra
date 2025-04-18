import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")


class Read_Config:
    @staticmethod
    def get_myntra_home_page_url():
        url = config.get('myntra_home_page','myntra_home_page_url')
        return url
