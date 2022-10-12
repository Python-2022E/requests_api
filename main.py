import requests
import json
class main:
    def __init__(self,response = requests.get('https://randomuser.me/api').json()):
        """Get element form randmouser.me
        Args:
            url (str, optional): _description_. Defaults to 'https://randomuser.me/api'.
        """
        self.response = response
    def refresh(self):
        """Refresh the site for get a new informations about users
        """
        self.response = requests.get('https://randomuser.me/api').json()

    def is_male(self):
        """Check the user is male or female

        Returns:
            bool: True if user is male
        """
        return self.response['results'][0]['gender']=='male'

    def get_elements(self):
        """Get elements function to determine male or female

        Returns:
            file:male_data.json and female_data.json
        """
        a=0
        while a!=10:
            if self.is_male():
                with open('male_data.json','a+') as f1:
                    f1.write(f"{json.dumps(self.response, indent=4)}\n")
                a+=1
                self.refresh()
            else:
                with open('female_data.json','a+') as f2:
                    f2.write(f"{json.dumps(self.response, indent=4)}\n")
                self.refresh()
        return 'Successfully!'

t1 = main()
print(t1.get_elements())