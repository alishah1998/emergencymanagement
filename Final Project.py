#!/usr/bin/env python
# coding: utf-8

# In[128]:


# Creating the map
import folium
import webbrowser

us_map = folium.Map(location=[39.8283, -98.5795], zoom_start=4)



# In[129]:


# Adding tile options for user to add
folium.TileLayer('Cartodb dark_matter').add_to(us_map)
folium.TileLayer('openstreetmap').add_to(us_map)

folium.LayerControl().add_to(us_map)


# In[130]:


# Alabama
folium.Marker([32.79736009937029, -86.56830802206882],
             popup='<h1> Alabama Emergency Management </h1> <p><a href="http://ema.alabama.gov/">Website</a></p>  <p>phone number: 205-280-2200</p>',
             tooltip='Alabama',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)


# Alaska
folium.Marker([61.269934751915635, -149.63792449461323],
             popup='<h1> Alaska Emergency Management </h1> <p><a href="https://ready.alaska.gov/">Website</a></p>  <p>phone number: 907-428-7606</p>',
             tooltip='Alaska',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map) 

# Arkansas
folium.Marker([34.83020624927771, -92.28554525305465],
             popup='<h1> Arkansas Emergency Management </h1> <p><a href="http://www.adem.arkansas.gov/">Website</a></p>  <p>phone number: 501-683-6700</p>',
             tooltip='Arkansas',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# California
folium.Marker([38.570008426833255, -121.30543020707059],
             popup='<h1> California Emergency Management </h1> <p><a href="caloes.ca.gov">Website</a></p>  <p>phone number: 916-845-8510</p>',
             tooltip='Califronia',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# Colorado
folium.Marker([39.58100008695532, -104.88468964637731],
             popup='<h1> Colorado Emergency Management </h1> <p><a href="https://cdphe.colorado.gov/emergency-preparedness-response">Website</a></p>  <p>phone number: 720-852-6600</p>',
             tooltip='Colorado',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# Connecticut
folium.Marker([41.569398406125515, -72.72757739376682],
             popup='<h1> Connecticut Emergency Management </h1> <p><a href="https://portal.ct.gov/demhs">Website</a></p>  <p>phone number: 860-685-8531</p>',
             tooltip='Connecticut',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# Delaware
folium.Marker([39.31963264715672, -75.60713198471603],
             popup='<h1> Delaware Emergency Management </h1> <p><a href="https://dema.delaware.gov/">Website</a></p>  <p>phone number: 302-659-3362</p>',
             tooltip='Delaware',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# District of Colombia
folium.Marker([38.854383375321774, -76.99517140658934],
             popup='<h1> District of Colmbia Emergency Management </h1> <p><a href="https://hsema.dc.gov/">Website</a></p>  <p>phone number: 202-727-6161</p>',
             tooltip='District of Colmbia',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# Florida
folium.Marker([30.394849712382317, -84.2329350729193],
             popup='<h1> Florida Emergency Management </h1> <p><a href="https://www.floridadisaster.org/">Website</a></p>  <p>phone number: 850-413-9969</p>',
             tooltip='Florida',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# Georgia
folium.Marker([33.86881622541791, -84.25114689901939],
             popup='<h1> Georgia Emergency Management </h1> <p><a href="https://www.usa.gov/state-emergency-management">Website</a></p>  <p>phone number: 404-635-7200</p>',
             tooltip='Georgia',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# Hawaii
folium.Marker([23.36867639720465, -157.8170800683515],
             popup='<h1> Hawaii Emergency Management </h1> <p><a href="https://dod.hawaii.gov/hiema/hiema-leadership/">Website</a></p>  <p>phone number: 808-733-4300</p>',
             tooltip='Hawaii',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# Idaho
folium.Marker([43.55781634311303, -116.23192590713717],
             popup='<h1> Idaho Emergency Management </h1> <p><a href="https://ioem.idaho.gov/">Website</a></p>  <p>phone number: 208-258-6500</p>',
             tooltip='Idaho',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# Illinois
folium.Marker([43.55781634311303, -116.23192590713717],
             popup='<h1> Illinois Emergency Management </h1> <p><a href="https://iemaohs.illinois.gov/">Website</a></p>  <p>phone number: 208-258-6500</p>',
             tooltip='Illinois',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# Indiana
folium.Marker([39.768043171404926, -86.16532672941221],
             popup='<h1> Indiana Emergency Management </h1> <p><a href="https://www.in.gov/dhs/">Website</a></p>  <p>phone number: 1-800-457-8283</p>',
             tooltip='Indiana',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# Iowa
folium.Marker([39.768043171404926, -86.16532672941221],
             popup='<h1> Iowa Emergency Management </h1> <p><a href="https://homelandsecurity.iowa.gov/">Website</a></p>  <p>phone number: 515-725-3231 </p>',
             tooltip='Iowa',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# Kansas
folium.Marker([39.1013719725776, -94.65141480770035],
             popup='<h1> Kansas Emergency Management </h1> <p><a href="https://www.kansastag.gov/kdem_default.asp">Website</a></p>  <p>phone number: 785-646-0092 </p>',
             tooltip='Kansas',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# Kentucky
folium.Marker([38.21611799350233, -84.90499333873922],
             popup='<h1> Kentucky Emergency Management </h1> <p><a href="https://kyem.ky.gov/Pages/default.aspx">Website</a></p>  <p>phone number: 800-255-2587 </p>',
             tooltip='Kentucky',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# Louisiana
folium.Marker([30.580997046686306, -90.73603721850924],
             popup='<h1> Louisiana Emergency Management </h1> <p><a href="https://gohsep.la.gov/">Website</a></p>  <p>phone number: 225-686-3066 </p>',
             tooltip='Louisiana',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# Maine
folium.Marker([44.366917518922136, -69.80007800802244],
             popup='<h1> Maine Emergency Management </h1> <p><a href="https://www.maine.gov/mema/">Website</a></p>  <p>phone number: 207-624-4400 </p>',
             tooltip='Maine',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# Maryland
folium.Marker([44.366917518922136, -69.80007800802244],
             popup='<h1> Maryland Emergency Management </h1> <p><a href="https://mdem.maryland.gov/Pages/default.aspx">Website</a></p>  <p>phone number: 1-877-636-2872 </p>',
             tooltip='Maryland',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# Massachusetts
folium.Marker([44.46415396613081, -69.85280041119826],
             popup='<h1> Massachusetts Emergency Management </h1> <p><a href="https://www.mass.gov/orgs/massachusetts-emergency-management-agency">Website</a></p>  <p>phone number: 508-820-2000 </p>',
             tooltip='Massachusetts',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# Michigan
folium.Marker([44.46415396613081, -69.85280041119826],
             popup='<h1> Michigan Emergency Management </h1> <p><a href="https://www.michigan.gov/msp/divisions/emhsd">Website</a></p>  <p>phone number: 800-621-3362 </p>',
             tooltip='Michigan',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# Minnesota
folium.Marker([42.64653727521445, -82.88091365001938],
             popup='<h1> Minnesota Emergency Management </h1> <p><a href="https://www.michigan.gov/msp/divisions/emhsd">Website</a></p>  <p>phone number: 800-621-3362 </p>',
             tooltip='Minnesota',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# Mississippi
folium.Marker([32.246775687754784, -90.0947322689957],
             popup='<h1> Mississippi Emergency Management </h1> <p><a href="https://www.msema.org/">Website</a></p>  <p>phone number: 601-933-6362 </p>',
             tooltip='Mississippi',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# Missouri
folium.Marker([38.64075890859697, -92.10824145088624],
             popup='<h1> Missouri Emergency Management </h1> <p><a href="https://sema.dps.mo.gov/">Website</a></p>  <p>phone number: 573-526-9100 </p>',
             tooltip='Missouri',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# Montana
folium.Marker([46.77857920363529, -112.0579543092746],
             popup='<h1> Montana Emergency Management </h1> <p><a href="https://des.mt.gov/">Website</a></p>  <p>phone number: 406-324-4777 </p>',
             tooltip='Montana',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# Nebraska
folium.Marker([42.302986945694876, -103.28097597185032],
             popup='<h1> Nebraska Emergency Management </h1> <p><a href="http://www.scottsbluffcounty.org/emergency-management/emergency-management.html">Website</a></p>  <p>phone number: 308-436-6689 </p>',
             tooltip='Nebraska',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# Nevada
folium.Marker([39.728885813285736, -119.55502482301495],
             popup='<h1> Nevada Emergency Management </h1> <p><a href="https://dem.nv.gov/">Website</a></p>  <p>phone number: 775-687-0300 </p>',
             tooltip='Nevada',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# New Hampshire
folium.Marker([43.24202831650685, -71.20224146920673],
             popup='<h1> New Hampshire Emergency Management </h1> <p><a href="https://www.nh.gov/safety/divisions/hsem/">Website</a></p>  <p>phone number: 1-800-735-2964 </p>',
             tooltip='New Hampshire',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# New Jersey
folium.Marker([40.90624897765808, -73.98347297487959],
             popup='<h1> New Jersey Emergency Management </h1> <p><a href="https://www.nj.gov/njoem/">Website</a></p>  <p>phone number: 201-547-5681 </p>',
             tooltip='New Jersey',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# New Mexico
folium.Marker([37.135296505864076, -105.2034336858739],
             popup='<h1> New Mexico Emergency Management </h1> <p><a href="https://www.nmdhsem.org/">Website</a></p>  <p>phone number: 505-476-9600 </p>',
             tooltip='New Mexico',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# New York
folium.Marker([40.7250623181633, -73.99826424197308],
             popup='<h1> New York Emergency Management </h1> <p><a href="https://www.dhses.ny.gov/office-emergency-management">Website</a></p>  <p>phone number: 212-639-9675 </p>',
             tooltip='New York',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# North Carolina
folium.Marker([36.2270609528734, -78.78441348329665],
             popup='<h1> North Carolina Emergency Management </h1> <p><a href="https://www.ncdps.gov/our-organization/emergency-management">Website</a></p>  <p>phone number: 919-825-2500 </p>',
             tooltip='North Carolina',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# North Dakota
folium.Marker([48.09996767977272, -100.3597916135649],
             popup='<h1> North Dakota Emergency Management </h1> <p><a href="https://www.des.nd.gov/">Website</a></p>  <p>phone number: 701-328-8100 </p>',
             tooltip='North Dakota',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# North Dakota
folium.Marker([48.09996767977272, -100.3597916135649],
             popup='<h1> North Dakota Emergency Management </h1> <p><a href="https://www.des.nd.gov/">Website</a></p>  <p>phone number: 701-328-8100 </p>',
             tooltip='North Dakota',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# Ohio
folium.Marker([40.18457887891765, -83.04481203411835],
             popup='<h1> Ohio Emergency Management </h1> <p><a href="https://ema.ohio.gov/">Website</a></p>  <p>phone number: 614-889-7150 </p>',
             tooltip='Ohio',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# Oklahoma
folium.Marker([35.60631662884928, -97.50517354034584],
             popup='<h1> Oklahoma Emergency Management </h1> <p><a href="https://oklahoma.gov/oem.html">Website</a></p>  <p>phone number: 405-521-2481 </p>',
             tooltip='Oklahoma',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# Oregon
folium.Marker([44.90157621189059, -123.01166684611314],
             popup='<h1> Oregon Emergency Management </h1> <p><a href="oregon.gov/OEM/Pages/default.aspx">Website</a></p>  <p>phone number: 503-378-2911 </p>',
             tooltip='Oregon',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# Pennsylvania
folium.Marker([40.36297291602036, -76.85545938558256],
             popup='<h1> Pennsylvania Emergency Management </h1> <p><a href="https://www.pema.pa.gov/Pages/Default.aspx#.VSPi6_nF-aU">Website</a></p>  <p>phone number: 717-651-2001 </p>',
             tooltip='Pennsylvania',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# Puerto Rico
folium.Marker([18.7809138443849, -66.05230387693237],
             popup='<h1> Puerto Rico Emergency Management </h1> <p><a href="https://manejodeemergencias.pr.gov/">Website</a></p>  <p>phone number: 787-724-0124 </p>',
             tooltip='Puerto Rico',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# Rhode Island
folium.Marker([41.74967361049758, -71.46848025572724],
             popup='<h1> Rhode Island Emergency Management </h1> <p><a href="https://riema.ri.gov/">Website</a></p>  <p>phone number: 401-946-9996 </p>',
             tooltip='Rhode Island',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# South Carolina
folium.Marker([34.324156174793146, -81.27337852794044],
             popup='<h1> South Carolina Emergency Management </h1> <p><a href="https://www.scemd.org/">Website</a></p>  <p>phone number: 803-737-8500 </p>',
             tooltip='South Carolina',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# South Dakota
folium.Marker([44.005751955841276, -97.11203594573855],
             popup='<h1> South Dakota Emergency Management </h1> <p><a href="https://dps.sd.gov/emergency-services/emergency-management">Website</a></p>  <p>phone number: 605-256-7611 </p>',
             tooltip='South Dakota',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# Tennessee
folium.Marker([36.17700883761123, -86.81063480110802],
             popup='<h1> Tennessee Emergency Management </h1> <p><a href="https://www.tn.gov/tema.html">Website</a></p>  <p>phone number: 615-741-0001 </p>',
             tooltip='Tennessee',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# Texas
folium.Marker([31.021813204692112, -97.40151111166023],
             popup='<h1> Texas Emergency Management </h1> <p><a href="https://emergency.portal.texas.gov/">Website</a></p>  <p>phone number: 512-424-2208 </p>',
             tooltip='Texas',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# U.S. Virgin Islands
folium.Marker([18.375956928552924, -64.96287194078747],
             popup='<h1> U.S. Virgin Islands Emergency Management </h1> <p><a href="https://vitema.vi.gov/">Website</a></p>  <p>phone number: 340-712-6299 </p>',
             tooltip='U.S. Virgin Islands',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# Utah
folium.Marker([40.691367122789494, -111.9604186269198],
             popup='<h1> Utah Emergency Management </h1> <p><a href="dem.utah.gov">Website</a></p>  <p>phone number: 801-538-3400 </p>',
             tooltip='Utah',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# Vermont
folium.Marker([44.33061830160541, -72.75064408585513],
             popup='<h1> Vermont Emergency Management </h1> <p><a href="https://vem.vermont.gov/">Website</a></p>  <p>phone number: 800-347-0488 </p>',
             tooltip='Vermont',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# Virginia
folium.Marker([37.57874494934837, -77.59666453565418],
             popup='<h1> Virginia Emergency Management </h1> <p><a href="https://www.virginia.gov/agencies/department-of-emergency-management/">Website</a></p>  <p>phone number: 804-267-7600 </p>',
             tooltip='Virginia',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# Washington
folium.Marker([47.81515995046155, -122.32245913910478],
             popup='<h1> Washington Emergency Management </h1> <p><a href="https://mil.wa.gov/emergency-management-division">Website</a></p>  <p>phone number: 253-512-7000 </p>',
             tooltip='Washington',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# West Virginia
folium.Marker([39.7937238700262, -80.84989263018775],
             popup='<h1> West Virginia Emergency Management </h1> <p><a href="https://emd.wv.gov/Pages/default.aspx">Website</a></p>  <p>phone number: 304-558-5380 </p>',
             tooltip='West Virginia',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# Wisconsin
folium.Marker([43.131223774713, -89.3314245358931],
             popup='<h1> Wisconsin Emergency Management </h1> <p><a href="https://wem.wi.gov/">Website</a></p>  <p>phone number: 608-242-3000 </p>',
             tooltip='Wisconsin',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)

# Wyoming
folium.Marker([41.60737789340945, -104.55097294317319],
             popup='<h1> Wyoming Emergency Management </h1> <p><a href="https://hls.wyo.gov/">Website</a></p>  <p>phone number: 307-777-4900 </p>',
             tooltip='Wyoming',
             icon=folium.Icon(icon='heart', icon_color='red')).add_to(us_map)


# In[131]:


# Save the map as an HTML file
us_map.save("us_state_map.html")

# Open the HTML file in a new browser window
webbrowser.open("us_state_map.html", new=2)


# In[ ]:





# In[ ]:




