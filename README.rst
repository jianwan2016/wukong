======
wukong
======


General Purpose Data Pipeline to deliver the collected data to data store.


Description
===========

* Pipeline model
`Data Source` ---> `Kafka Topic` ---> `Data Sink`

* Protobuf based
Use protobuf to define the message shared between source and sink

* Data Source
Any application generating structured data

* Data Sink
Any data store either SQL or NOSQL, currently only support postgresql

* Usage scenario
One example is WebsiteMonitor, collecting website status data and deliver it to postgresql, see `apps/website_mornitor`