======
wukong
======


General Purpose Data Pipeline to deliver the collected data to data store.


Description
===========

* Pipeline model
**Data Source ---> Kafka Topic ---> Data Sink**

* Protobuf based
Use protobuf to define the message shared between source and sink

* Data Source
Any application generating structured data. It can scale.

* Data Sink
Any data store either SQL or NOSQL, currently only support postgresql. It can scale.

* Usage scenario
One example is WebsiteMonitor, collecting website status data and deliver it to postgresql, see `apps/website_mornitor`

WebsiteMonitor
===========
* Create virtualenv in terminal:
  ::
    virtualenv website-monitor
    source bin/activate

* Start data source in one terminal:
  ::
    python website_data_source.py

* Start data sink in another terminal:
  ::
    python website_data_sink.py

* Observe:
  There are logs output in sink terminal:
  ::

    base {
    service_name: "website_monitor"
    timestamp: 1593606239415
    }
    monitor_id: "test_client_1"
    website: "aiven.io"
    response_time: 1049
    status_code: 200
  
  

  And check the db records:
  ::
    In [6]: c.execute('SELECT * from status limit 5')

    In [7]:
    
    In [7]: c.fetchall()
    Out[7]:
    [(1593602083332, 'test_client_1', 'aiven.io', 1085, 200),
     (1593602094405, 'test_client_1', 'aiven.io', 1123, 200),
     (1593602106131, 'test_client_1', 'aiven.io', 1151, 200),
     (1593602140293, 'test_client_1', 'aiven.io', 1123, 200),
     (1593602142554, 'test_client_1', 'aiven.io', 1073, 200)]
    
    In [8]: c.execute('SELECT count(*) from status')
    
    In [9]: c.fetchall()
    Out[9]: [(1972,)]


TODOs
===========
* Complete unit test
* Dockerise
* Signal handling
