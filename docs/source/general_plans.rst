General plan
============

SPBGTI tools services plan and decisions (EPIC)
###############################################

:Language:  Python 3.5

:Platform:  Django

:Server:  Ubuntu/Debian Linux with Docker Swarm (servers > 2 for load balancing)

:Database:  Not decided yet, at this point that’s SQLite, but should be changed to some object-oriented later

:Architecture:  Micro services

:Features:

+ Scheduling feature;
+ Library service feature;
+ Calendar planning service.

All these features should be made as a **RESTful** services and independent.

