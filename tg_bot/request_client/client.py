import requests

from config import Settings


class Client:
    URL: str = Settings.URL_API
    TIMEOUT: int = 5

    def get_musician_response(self, params):
        response = requests.session().get(self.URL + Settings.MUSICIAN + params, timeout=self.TIMEOUT)
        return response.json()


    def list_musician(self):
        response = requests.session().get(self.URL + Settings.MUSICIAN)
        return response.json()


    def add_musician(self, data):
        response = requests.session().post(
            url=self.URL + Settings.MUSICIAN,
            data=data,
            headers={'content-type': 'application/json'},
            timeout=self.TIMEOUT
        )
        if response.status_code == 201:
            return "Анкета успешно создана."
        else:
            raise ValueError('Wrong params. Response message: {}'.format(response.json()))


    def get_musicians_tg_id(self):
        response = requests.get(
            self.URL + Settings.TG_MUSICIAN,
            timeout=self.TIMEOUT
        )
        return response.json()


    def get_bands_response(self, params):
        response = requests.session().get(self.URL + Settings.BAND + params, timeout=self.TIMEOUT)
        return response.json()


    def get_bands_tg_id(self):
        response = requests.get(
            self.URL + Settings.TG_BAND,
            timeout=self.TIMEOUT
        )
        return response.json()


    def add_band(self, data):
        response = requests.session().post(
            url=self.URL + Settings.BAND,
            data=data,
            headers={'content-type': 'application/json'},
            timeout=self.TIMEOUT
        )
        if response.status_code == 201:
            return "Анкета успешно создана."


    def list_band(self):
        response = requests.session().get(self.URL + Settings.BAND, timeout=self.TIMEOUT)
        return response.json()


    def get_my_profile(self, user_id):
        response = requests.session().get(
            url=self.URL + Settings.PROFILE + user_id,
            timeout=self.TIMEOUT
        )
        return response.json()

    def delete_profile(self, endpoint, pk):
        response = requests.session().delete(
            url=f'{self.URL}{endpoint}{str(pk)}/',
            headers={'content-type': 'application/json'},
            timeout=self.TIMEOUT
        )
        print(response.status_code)
        return(f"Анкета удалена. status_code {str(response.status_code)}")
