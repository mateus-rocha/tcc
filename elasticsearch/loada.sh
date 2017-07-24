#!/bin/sh
curl -XPUT http://localhost:9200/_template/kafka -d '
{
    "template":"kafka-*",
        "mappings": {
	    "logs": {
	        "properties":{
		    "ip_src":{"type":"ip"},
		    "ip_dst":{"type":"ip"},
		    "dns_a":{"type":"ip"},
		    "geoip_ip_dst":{
			"properties":{
			    "area_code":{"type":"long"},
			    "asn":{"type":"string"},
			    "city_name":{"type":"string"},
			    "continent_code":{"type":"string"},
			    "country_code2":{"type":"string"},
                  	    "country_code3":{"type":"string"},
                  	    "country_name":{"type":"string", "index":"not_analyzed"},
                  	    "dma_code":{"type":"long"},
                  	    "ip":{"type":"ip"},
                  	    "latitude":{"type":"double"},
                  	    "location":{"type":"geo_point"},
                  	    "longitude":{"type":"double"},
                  	    "number":{"type":"string"},
                  	    "postal_code":{"type":"string"},
                  	    "real_region_name":{"type":"string", "index":"not_analyzed"},
                  	    "region_name":{"type":"string", "index":"not_analyzed"},
                  	    "timezone":{"type":"string"}
			}
		    },
		    "geoip_ip_src":{
                        "properties":{
                            "area_code":{"type":"long"},
                            "asn":{"type":"string"},
                            "city_name":{"type":"string"},
                            "continent_code":{"type":"string"},
                            "country_code2":{"type":"string"},
                            "country_code3":{"type":"string"},
                            "country_name":{"type":"string", "index":"not_analyzed"},
                            "dma_code":{"type":"long"},
                            "ip":{"type":"ip"},
                            "latitude":{"type":"double"},
                            "location":{"type":"geo_point"},
                            "longitude":{"type":"double"},
                            "number":{"type":"string"},
                            "postal_code":{"type":"string"},
                            "real_region_name":{"type":"string", "index":"not_analyzed"},
                            "region_name":{"type":"string", "index":"not_analyzed"},
                            "timezone":{"type":"string"}
                        }
                    },
		    "geoip_dns_a":{
                        "properties":{
                            "area_code":{"type":"long"},
                            "asn":{"type":"string"},
                            "city_name":{"type":"string"},
                            "continent_code":{"type":"string"},
                            "country_code2":{"type":"string"},
                            "country_code3":{"type":"string"},
                            "country_name":{"type":"string", "index":"not_analyzed"},
                            "dma_code":{"type":"long"},
                            "ip":{"type":"ip"},
                            "latitude":{"type":"double"},
                            "location":{"type":"geo_point"},
                            "longitude":{"type":"double"},
                            "number":{"type":"string"},
                            "postal_code":{"type":"string"},
                            "real_region_name":{"type":"string", "index":"not_analyzed"},
                            "region_name":{"type":"string", "index":"not_analyzed"},
                            "timezone":{"type":"string"}
                        }
                    },
			"geoip_http_host":{
                        "properties":{
                            "area_code":{"type":"long"},
                            "asn":{"type":"string"},
                            "city_name":{"type":"string"},
                            "continent_code":{"type":"string"},
                            "country_code2":{"type":"string"},
                            "country_code3":{"type":"string"},
                            "country_name":{"type":"string", "index":"not_analyzed"},
                            "dma_code":{"type":"long"},
                            "ip":{"type":"ip"},
                            "latitude":{"type":"double"},
                            "location":{"type":"geo_point"},
                            "longitude":{"type":"double"},
                            "number":{"type":"string"},
                            "postal_code":{"type":"string"},
                            "real_region_name":{"type":"string", "index":"not_analyzed"},
                            "region_name":{"type":"string", "index":"not_analyzed"},
                            "timezone":{"type":"string"}
                        }
                    }
		}
	    }
	}
}'
