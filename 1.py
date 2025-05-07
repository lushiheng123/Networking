import meraki
API_KEY = "a55f85b1b95936dfeca51bc1ed96a5ba3f495438"
org_id = 1684610
dashboard = meraki.DashboardAPI(API_KEY)
response = dashboard.organizations.getOrganizationNetworks(org_id)
print(response)
