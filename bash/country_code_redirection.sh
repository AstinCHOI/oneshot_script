#!/bin/bash

# TODO: 
# Recursive redirection

# INPUT
domain=""

# OUTPUT
for code in kr us ru ca kw ae om af ye sy ps jo pk il bh iq lb ir qa
do
  ip=$(/usr/local/bin/sdig -n | awk -v x=$code '$NF>5 && $2==toupper(x) { print $(NF-5); }')
  if [ $code == "om" ]; then
    ip="82.178.158.31"
  fi
  echo "== $code =="
  echo "curl -s -I https://$domain/g90 -H'X-Forwarded-For: $ip'"
  curl -s -I "https://$domain/g90" -H"X-Forwarded-For: $ip" | egrep "Location"
done


## Result of sdig
# +--------------+-----------------------------------+-----------------+-----------------+------------+
# |                 Public DNS Server List - Last updated at 2017-02-11 10:38:47 UTC                  |
# +--------------+-----------------------------------+-----------------+-----------------+------------+
# | Country_code | Country                           | Ipaddress       | Availability(%) | Checked_at |
# +--------------+-----------------------------------+-----------------+-----------------+------------+
# | AL           | Albania                           | 91.226.220.254  | 100             | 2017-02-06 |
# | AD           | Andorra                           | 194.158.80.13   | 100             | 2017-02-07 |
# | AQ           | Antarctica                        | 185.121.177.177 | 90              | 2017-02-07 |
# | AS           | American Samoa                    | 202.70.112.74   | 86              | 2017-02-09 |
# | DZ           | Algeria                           | 193.251.169.83  | 100             | 2017-02-06 |
# | BF           | Burkina Faso                      | 196.28.245.26   | 100             | 2017-02-07 |
# | CV           | Cape Verde                        | 41.79.124.9     | 100             | 2017-02-07 |
# | IO           | British Indian Ocean Territory    | 203.83.53.32    | 90              | 2017-02-08 |
# | AW           | Aruba                             | 206.48.21.218   | 90              | 2017-02-07 |
# | AT           | Austria                           | 195.70.248.2    | 100             | 2017-02-07 |
# | BB           | Barbados                          | 66.249.145.225  | 90              | 2017-02-07 |
# | BD           | Bangladesh                        | 119.148.8.18    | 100             | 2017-02-06 |
# | BR           | Brazil                            | 187.45.155.249  | 100             | 2017-02-10 |
# | BI           | Burundi                           | 197.157.193.146 | 100             | 2017-02-06 |
# | CO           | Colombia                          | 190.242.99.21   | 100             | 2017-02-07 |
# | AM           | Armenia                           | 212.73.65.40    | 100             | 2017-02-06 |
# | BN           | Brunei Darussalam                 | 202.152.77.212  | 100             | 2017-02-07 |
# | BG           | Bulgaria                          | 213.91.153.9    | 100             | 2017-02-07 |
# | BJ           | Benin                             | 41.85.184.102   | 30              | 2017-02-07 |
# | AO           | Angola                            | 41.205.58.72    | 90              | 2017-02-07 |
# | HR           | Croatia                           | 195.29.217.173  | 100             | 2017-02-06 |
# | AU           | Australia                         | 119.17.48.189   | 100             | 2017-02-07 |
# | CN           | China                             | 210.2.4.8       | 100             | 2017-02-06 |
# | CA           | Canada                            | 208.79.112.4    | 100             | 2017-02-07 |
# | CY           | Cyprus                            | 194.154.133.222 | 100             | 2017-02-06 |
# | BE           | Belgium                           | 178.32.40.244   | 100             | 2017-02-06 |
# | BW           | Botswana                          | 83.143.29.165   | 100             | 2017-02-07 |
# | BH           | Bahrain                           | 89.148.14.227   | 100             | 2017-02-06 |
# | BZ           | Belize                            | 200.123.208.163 | 90              | 2017-02-06 |
# | AG           | Antigua and Barbuda               | 207.42.135.145  | 100             | 2017-02-07 |
# | CM           | Cameroon                          | 41.211.125.141  | 100             | 2017-02-07 |
# | AR           | Argentina                         | 190.105.237.175 | 100             | 2017-02-07 |
# | BA           | Bosnia and Herzegovina            | 77.78.200.5     | 100             | 2017-02-06 |
# | BO           | Bolivia, Plurinational State of   | 186.2.37.97     | 100             | 2017-02-06 |
# | AZ           | Azerbaijan                        | 95.86.129.170   | 100             | 2017-02-06 |
# | KY           | Cayman Islands                    | 200.11.138.101  | 100             | 2017-02-07 |
# | BY           | Belarus                           | 212.98.160.50   | 100             | 2017-02-06 |
# | CL           | Chile                             | 186.67.20.35    | 100             | 2017-02-07 |
# | CR           | Costa Rica                        | 200.122.151.247 | 100             | 2017-02-06 |
# | KH           | Cambodia                          | 202.8.73.136    | 100             | 2017-02-06 |
# | AI           | Anguilla                          | 204.14.249.58   | 100             | 2017-02-07 |
# | BS           | Bahamas                           | 24.244.148.152  | 100             | 2017-02-06 |
# | BM           | Bermuda                           | 162.255.216.44  | 100             | 2017-02-07 |
# | AF           | Afghanistan                       | 137.59.120.17   | 90              | 2017-02-08 |
# | CZ           | Czech Republic                    | 91.218.189.170  | 100             | 2017-02-07 |
# | CI           | Côte d'Ivoire                     | 196.47.169.76   | 100             | 2017-02-07 |
# | DK           | Denmark                           | 94.18.254.13    | 100             | 2017-02-06 |
# | DJ           | Djibouti                          | 41.189.225.110  | 100             | 2017-02-07 |
# | DO           | Dominican Republic                | 181.36.9.45     | 100             | 2017-02-06 |
# | EC           | Ecuador                           | 190.57.150.150  | 100             | 2017-02-06 |
# | EG           | Egypt                             | 212.122.224.10  | 100             | 2017-02-06 |
# | SV           | El Salvador                       | 190.5.129.37    | 100             | 2017-02-06 |
# | GQ           | Equatorial Guinea                 | 197.149.168.76  | 100             | 2017-02-07 |
# | EE           | Estonia                           | 194.204.60.93   | 100             | 2017-02-06 |
# | ET           | Ethiopia                          | 213.55.96.148   | 100             | 2017-02-07 |
# | FJ           | Fiji                              | 27.123.168.13   | 100             | 2017-02-06 |
# | FI           | Finland                           | 178.33.144.61   | 100             | 2017-02-06 |
# | FR           | France                            | 89.87.173.102   | 100             | 2017-02-07 |
# | PF           | French Polynesia                  | 113.197.68.20   | 100             | 2017-02-07 |
# | GA           | Gabon                             | 41.159.40.248   | 100             | 2017-02-07 |
# | GM           | Gambia                            | 197.148.74.19   | 100             | 2017-02-06 |
# | GE           | Georgia                           | 213.157.196.130 | 100             | 2017-02-06 |
# | DE           | Germany                           | 80.156.207.68   | 100             | 2017-02-07 |
# | GH           | Ghana                             | 41.74.84.1      | 100             | 2017-02-06 |
# | GR           | Greece                            | 193.92.92.194   | 100             | 2017-02-06 |
# | GL           | Greenland                         | 46.16.17.175    | 100             | 2017-02-07 |
# | GD           | Grenada                           | 216.110.114.137 | 90              | 2017-02-07 |
# | GP           | Guadeloupe                        | 81.248.21.47    | 80              | 2017-02-07 |
# | GU           | Guam                              | 202.151.80.211  | 100             | 2017-02-06 |
# | GT           | Guatemala                         | 190.56.249.189  | 100             | 2017-02-07 |
# | GN           | Guinea                            | 41.79.236.125   | 40              | 2017-02-07 |
# | GY           | Guyana                            | 190.124.220.41  | 100             | 2017-02-07 |
# | HN           | Honduras                          | 190.107.136.242 | 100             | 2017-02-06 |
# | HK           | Hong Kong                         | 14.199.54.3     | 100             | 2017-02-07 |
# | HT           | Haiti                             | 190.120.200.42  | 100             | 2017-02-06 |
# | HU           | Hungary                           | 82.141.171.222  | 100             | 2017-02-07 |
# | ID           | Indonesia                         | 103.23.244.136  | 100             | 2017-02-10 |
# | IS           | Iceland                           | 149.126.81.25   | 100             | 2017-02-06 |
# | IR           | Iran, Islamic Republic of         | 94.183.66.120   | 88              | 2017-02-08 |
# | IQ           | Iraq                              | 176.241.91.199  | 100             | 2017-02-07 |
# | IE           | Ireland                           | 83.70.180.238   | 100             | 2017-02-06 |
# | IL           | Israel                            | 31.168.224.100  | 100             | 2017-02-07 |
# | IN           | India                             | 125.63.77.210   | 100             | 2017-02-07 |
# | JM           | Jamaica                           | 208.138.22.42   | 100             | 2017-02-06 |
# | IT           | Italy                             | 81.30.21.201    | 100             | 2017-02-07 |
# | JO           | Jordan                            | 82.212.67.101   | 100             | 2017-02-06 |
# | JP           | Japan                             | 218.219.100.139 | 100             | 2017-02-07 |
# | KZ           | Kazakhstan                        | 178.90.136.102  | 100             | 2017-02-06 |
# | KE           | Kenya                             | 41.215.81.6     | 100             | 2017-02-06 |
# | KG           | Kyrgyzstan                        | 212.2.227.8     | 100             | 2017-02-06 |
# | KR           | Korea, Republic of                | 112.163.223.30  | 100             | 2017-02-07 |
# | LA           | Lao People's Democratic Republic  | 202.123.179.254 | 90              | 2017-02-06 |
# | KW           | Kuwait                            | 168.187.70.13   | 100             | 2017-02-06 |
# | LB           | Lebanon                           | 89.108.166.123  | 100             | 2017-02-07 |
# | LV           | Latvia                            | 95.130.37.86    | 100             | 2017-02-07 |
# | LR           | Liberia                           | 41.86.4.2       | 100             | 2017-02-07 |
# | LY           | Libya                             | 41.208.68.62    | 100             | 2017-02-07 |
# | LI           | Liechtenstein                     | 212.77.32.47    | 100             | 2017-02-07 |
# | LT           | Lithuania                         | 81.7.112.107    | 90              | 2017-02-08 |
# | LU           | Luxembourg                        | 195.46.239.58   | 100             | 2017-02-06 |
# | MO           | Macao                             | 202.175.89.60   | 100             | 2017-02-06 |
# | MK           | Macedonia, Republic of            | 194.149.146.2   | 100             | 2017-02-06 |
# | MG           | Madagascar                        | 41.204.105.78   | 80              | 2017-02-06 |
# | MW           | Malawi                            | 41.77.14.106    | 100             | 2017-02-07 |
# | MV           | Maldives                          | 124.195.199.2   | 90              | 2017-02-06 |
# | ML           | Mali                              | 196.200.80.86   | 100             | 2017-02-07 |
# | MY           | Malaysia                          | 203.223.150.5   | 100             | 2017-02-07 |
# | MT           | Malta                             | 195.158.96.145  | 100             | 2017-02-06 |
# | MQ           | Martinique                        | 81.248.8.14     | 100             | 2017-02-06 |
# | MR           | Mauritania                        | 82.151.74.36    | 100             | 2017-02-07 |
# | MU           | Mauritius                         | 196.192.81.61   | 100             | 2017-02-07 |
# | MX           | Mexico                            | 200.52.45.233   | 100             | 2017-02-07 |
# | FM           | Micronesia, Federated States of   | 119.252.118.16  | 90              | 2017-02-07 |
# | MC           | Monaco                            | 80.94.101.132   | 50              | 2017-02-07 |
# | MN           | Mongolia                          | 183.81.169.102  | 100             | 2017-02-07 |
# | MA           | Morocco                           | 81.192.160.133  | 100             | 2017-02-07 |
# | MD           | Moldova, Republic of              | 188.138.241.74  | 100             | 2017-02-07 |
# | MZ           | Mozambique                        | 196.3.99.130    | 100             | 2017-02-07 |
# | MM           | Myanmar                           | 203.81.161.9    | 100             | 2017-02-07 |
# | NA           | Namibia                           | 196.44.131.180  | 100             | 2017-02-07 |
# | NR           | Nauru                             | 203.98.228.115  | 100             | 2017-02-07 |
# | NL           | Netherlands                       | 188.207.200.113 | 100             | 2017-02-07 |
# | NP           | Nepal                             | 115.187.17.50   | 90              | 2017-02-06 |
# | NZ           | New Zealand                       | 203.109.129.68  | 100             | 2017-02-06 |
# | NI           | Nicaragua                         | 200.62.97.29    | 100             | 2017-02-07 |
# | NG           | Nigeria                           | 83.143.8.249    | 100             | 2017-02-06 |
# | NO           | Norway                            | 195.204.130.41  | 100             | 2017-02-06 |
# | PK           | Pakistan                          | 103.20.3.169    | 100             | 2017-02-06 |
# | PW           | Palau                             | 103.30.248.6    | 100             | 2017-02-07 |
# | PS           | Palestine, State of               | 212.14.239.252  | 100             | 2017-02-06 |
# | PA           | Panama                            | 190.34.220.171  | 100             | 2017-02-06 |
# | PG           | Papua New Guinea                  | 64.37.104.99    | 100             | 2017-02-06 |
# | PY           | Paraguay                          | 190.128.194.46  | 100             | 2017-02-07 |
# | PE           | Peru                              | 181.65.184.162  | 100             | 2017-02-06 |
# | PH           | Philippines                       | 203.115.130.74  | 100             | 2017-02-06 |
# | PL           | Poland                            | 193.107.250.56  | 100             | 2017-02-07 |
# | PT           | Portugal                          | 195.23.141.30   | 100             | 2017-02-07 |
# | PR           | Puerto Rico                       | 24.41.160.82    | 100             | 2017-02-06 |
# | QA           | Qatar                             | 78.100.88.188   | 100             | 2017-02-07 |
# | RO           | Romania                           | 89.165.155.168  | 100             | 2017-02-07 |
# | RU           | Russian Federation                | 85.175.226.5    | 100             | 2017-02-07 |
# | RW           | Rwanda                            | 197.243.96.3    | 80              | 2017-02-07 |
# | RE           | Réunion                           | 81.248.205.15   | 100             | 2017-02-07 |
# | KN           | Saint Kitts and Nevis             | 76.76.169.96    | 90              | 2017-02-07 |
# | LC           | Saint Lucia                       | 192.147.231.151 | 86              | 2017-02-09 |
# | PM           | Saint Pierre and Miquelon         | 70.36.0.5       | 100             | 2017-02-11 |
# | WS           | Samoa                             | 123.176.76.69   | 86              | 2017-02-09 |
# | SA           | Saudi Arabia                      | 46.152.9.200    | 100             | 2017-02-07 |
# | SN           | Senegal                           | 213.154.73.20   | 100             | 2017-02-06 |
# | SC           | Seychelles                        | 80.82.66.46     | 100             | 2017-02-07 |
# | SG           | Singapore                         | 203.125.210.171 | 100             | 2017-02-07 |
# | SK           | Slovakia                          | 37.9.168.137    | 100             | 2017-02-07 |
# | SI           | Slovenia                          | 194.249.60.2    | 100             | 2017-02-06 |
# | LK           | Sri Lanka                         | 124.43.25.209   | 100             | 2017-02-07 |
# | ZA           | South Africa                      | 41.86.112.35    | 100             | 2017-02-07 |
# | SD           | Sudan                             | 196.1.237.130   | 100             | 2017-02-06 |
# | ES           | Spain                             | 85.152.34.135   | 100             | 2017-02-07 |
# | SR           | Suriname                          | 186.179.192.205 | 86              | 2017-02-09 |
# | SE           | Sweden                            | 212.181.68.130  | 100             | 2017-02-07 |
# | CH           | Switzerland                       | 185.78.120.20   | 100             | 2017-02-07 |
# | SZ           | Swaziland                         | 196.24.66.192   | 90              | 2017-02-07 |
# | TW           | Taiwan, Province of China         | 163.20.127.1    | 100             | 2017-02-07 |
# | SY           | Syrian Arab Republic              | 91.144.22.198   | 100             | 2017-02-07 |
# | TJ           | Tajikistan                        | 85.9.129.38     | 100             | 2017-02-07 |
# | TH           | Thailand                          | 113.53.248.50   | 100             | 2017-02-07 |
# | TZ           | Tanzania, United Republic of      | 41.59.3.92      | 100             | 2017-02-07 |
# | TG           | Togo                              | 80.248.77.97    | 100             | 2017-02-07 |
# | TT           | Trinidad and Tobago               | 161.0.153.29    | 86              | 2017-02-09 |
# | TO           | Tonga                             | 202.43.9.12     | 90              | 2017-02-07 |
# | TN           | Tunisia                           | 41.226.17.228   | 100             | 2017-02-07 |
# | TR           | Turkey                            | 94.73.158.62    | 100             | 2017-02-07 |
# | TM           | Turkmenistan                      | 217.174.227.242 | 100             | 2017-02-07 |
# | UG           | Uganda                            | 41.138.2.1      | 100             | 2017-02-06 |
# | TC           | Turks and Caicos Islands          | 162.212.12.235  | 86              | 2017-02-09 |
# | AE           | United Arab Emirates              | 94.200.59.205   | 100             | 2017-02-06 |
# | UA           | Ukraine                           | 159.224.108.213 | 100             | 2017-02-07 |
# | GB           | United Kingdom                    | 217.10.130.10   | 100             | 2017-02-07 |
# | US           | United States                     | 66.216.18.222   | 100             | 2017-02-11 |
# | UY           | Uruguay                           | 200.40.174.173  | 100             | 2017-02-06 |
# | UZ           | Uzbekistan                        | 213.206.43.221  | 100             | 2017-02-06 |
# | VE           | Venezuela, Bolivarian Republic of | 200.62.19.140   | 100             | 2017-02-06 |
# | VG           | Virgin Islands, British           | 162.212.15.126  | 86              | 2017-02-09 |
# | VI           | Virgin Islands, U.S.              | 146.226.228.19  | 100             | 2017-02-07 |
# | VN           | Viet Nam                          | 203.128.242.40  | 100             | 2017-02-07 |
# | YE           | Yemen                             | 109.200.185.144 | 25              | 2017-02-08 |
# | ZM           | Zambia                            | 197.220.206.100 | 100             | 2017-02-07 |
# | ZW           | Zimbabwe                          | 41.78.79.118    | 100             | 2017-02-07 |
# +--------------+-----------------------------------+-----------------+-----------------+------------+