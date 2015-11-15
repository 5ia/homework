import requests
import unittest


class TestUpdate(unittest.TestCase):
    
    valid_usr='myself'
    valid_pass='mypass'
    app_name='MyApp'
    domain="https://my.domain.com"
    appId = '123'
    permissions = [ "A", "C" ] #WHAT ARE THE VALID PERMISSIONS? ARE THERE INVALID ONES AS WELL?
    inv_usr='john' #user that is not registered
    inv_pass='random'
    usr2='ben'
    psw2='benspass'
    app_new_name='MyNewApp'
    new_domain="https://my.newdomain.com"
    inv_appId="8979" # there should be no app with this ID
    
    def test_valid_auth_data(self):
        """ Test with correct authentication and valid data"""
        mydata = {"name" : self.app_name, "domain" : self.domain, "permissions" : self.permissions}
        url = self.domain + '/apps/' + self.appId
        r=requests.put(url,data=mydata, auth=(self.valid_usr, self.valid_pass))
        self.assertEqual(r.status_code, 200)
    def test_missing_auth(self):
        """ Test request without any authentication"""
        mydata = {"name" : self.app_name, "domain" : self.domain, "permissions" : self.permissions}
        url = self.domain + '/apps/' + self.appId
        r=requests.put(url,data=mydata)
        self.assertEqual(r.status_code,403)
    def test_missing_usr(self):
        """ Test request without user value passed in auth"""
        mydata = {"name" : self.app_name, "domain" : self.domain, "permissions" : self.permissions}
        url = self.domain + '/apps/' + self.appId
        r=requests.put(url,data=mydata, auth=('', self.valid_pass))
        self.assertEqual(r.status_code,403)
    def test_missing_pass(self):
        """ Test request without password value passed in auth"""
        mydata = {"name" : self.app_name, "domain" : self.domain, "permissions" : self.permissions}
        url = self.domain + '/apps/' + self.appId
        r=requests.put(url,data=mydata, auth=(self.valid_usr, ''))
        self.assertEqual(r.status_code,403)
    def test_wrong_usr(self):
        """ Test request with unexisting user value passed in auth"""
        mydata = {"name" : self.app_name, "domain" : self.domain, "permissions" : self.permissions}
        url = self.domain + '/apps/' + self.appId
        r=requests.put(url,data=mydata, auth=(self.inv_usr, self.valid_pass))
        self.assertEqual(r.status_code,403)
    def test_wrong_pass(self):
        """ Test request with incorrect password value passed in auth"""
        mydata = {"name" : self.app_name, "domain" : self.domain, "permissions" : self.permissions}
        url = self.domain + '/apps/' + self.appId
        r=requests.put(url,data=mydata, auth=(self.valid_usr, self.inv_pass))
        self.assertEqual(r.status_code,403)
    def test_wrong_owner(self):
        """ Test request with user that is not the owner of the app"""
        mydata = {"name" : self.app_name, "domain" : self.domain, "permissions" : self.permissions}
        url = self.domain + '/apps/' + self.appId
        r=requests.put(url,data=mydata, auth=(self.usr2, self.psw2))
        self.assertEqual(r.status_code,403)
    def test_name_update(self):
        """ Test request trying to update application name"""
        mydata = {"name" : self.app_new_name, "domain" : self.domain, "permissions" : self.permissions}
        url = self.domain + '/apps/' + self.appId
        r=requests.put(url,data=mydata, auth=(self.valid_usr, self.valid_pass))
        self.assertEqual(r.status_code,403)
    def test_domain_update(self):
        """ Test request trying to update domain name"""
        mydata = {"name" : self.app_name, "domain" : self.new_domain, "permissions" : self.permissions}
        url = self.domain + '/apps/' + self.appId
        r=requests.put(url,data=mydata, auth=(self.valid_usr, self.valid_pass))
        self.assertEqual(r.status_code,403)
    def test_missing_body(self):
        """ Test request without a body"""
        url = self.domain + '/apps/' + self.appId
        r=requests.put(url, auth=(self.valid_usr, self.valid_pass))
        self.assertEqual(r.status_code,400)
    def test_missing_appname(self):
        """ Test request without app name"""
        mydata = { "domain" : self.domain, "permissions" : self.permissions}
        url = self.domain + '/apps/' + self.appId
        r=requests.put(url,data=mydata, auth=(self.valid_usr, self.valid_pass))
        self.assertEqual(r.status_code,400)
    def test_missing_domain(self):
        """ Test request without a domain"""
        mydata = {"name" : self.app_name, "permissions" : self.permissions}
        url = self.domain + '/apps/' + self.appId
        r=requests.put(url,data=mydata, auth=(self.valid_usr, self.valid_pass))
        self.assertEqual(r.status_code,400)
    def test_missing_perms(self):
        """ Test request without permissions part"""
        mydata = {"name" : self.app_name, "domain" : self.domain}
        url = self.domain + '/apps/' + self.appId
        r=requests.put(url,data=mydata, auth=(self.valid_usr, self.valid_pass))
        self.assertEqual(r.status_code,400)
    def test_unknown_element(self):
        """ Test request with additional part in body that is not defined in specs"""
        mydata = {"name" : self.app_name, "domain" : self.domain, "permissions" : self.permissions, "new_option": "myoption"}
        url = self.domain + '/apps/' + self.appId
        r=requests.put(url,data=mydata, auth=(self.valid_usr, self.valid_pass))
        self.assertEqual(r.status_code,400)
    def test_missing_appid(self):
        """ Test request without application Id"""
        mydata = {"name" : self.app_name, "domain" : self.domain, "permissions" : self.permissions}
        url = self.domain + '/apps/' 
        r=requests.put(url,data=mydata, auth=(self.valid_usr, self.valid_pass))
        self.assertEqual(r.status_code,500)
    def test_missing_app(self):
        """ Test request for non-existant application"""
        mydata = {"name" : self.app_name, "domain" : self.domain, "permissions" : self.permissions}
        url = self.domain + '/apps/' + self.inv_appId
        r=requests.put(url,data=mydata, auth=(self.valid_usr, self.valid_pass))
        self.assertEqual(r.status_code,404)
        


if __name__ == '__main__':
    unittest.main()