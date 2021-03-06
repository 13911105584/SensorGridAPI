from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from sensordata.models import SensorData
from sensordata.serializers import *
from sensordata.models import SensorData
import datetime

@api_view(['GET', 'POST'])
def sensordata_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        sensordata = SensorData.objects.all()

        # **********************************************
        # for filtering data by certain field conditions
        # **********************************************
        # http://127.0.0.1:8000/sensordata/?node_id=<INT>
        if 'node_id' in request.GET:
            sensordata = sensordata.filter(node_id = request.GET['node_id'])
        # http://127.0.0.1:8000/sensordata/?created_at_gt=<EPOCH>

        elif 'created_at_gt' in request.GET:
            dt = datetime.datetime.fromtimestamp(int(request.GET['created_at_gt']))
            sensordata = sensordata.filter(created_at__gt = dt)
        # http://127.0.0.1:8000/sensordata/?created_at_lt=<EPOCH>

        elif 'created_at_lt' in request.GET:
            dt = datetime.datetime.fromtimestamp(int(request.GET['created_at_lt']))
            sensordata = sensordata.filter(created_at__lt = dt)

        # *******************************************
        # for only showing certain fields of the data
        # *******************************************
        if 'battery' in request.GET:
            # http://127.0.0.1:8000/sensordata/?battery&created_at
            if 'created_at' in request.GET:
                serializer = SensorDataSerializer_battery_created_at(sensordata, many=True)

            # http://127.0.0.1:8000/sensordata/?battery&node_id_include
            elif 'node_id_include' in request.GET:
                serializer = SensorDataSerializer_battery_node_id(sensordata, many=True)

            # http://127.0.0.1:8000/sensordata/?battery
            else:
                serializer = SensorDataSerializer_battery(sensordata, many=True)

        # http://127.0.0.1:8000/sensordata/?data
        elif 'data' in request.GET:
            if 'node_id_include' in request.GET:

                # http://127.0.0.1:8000/sensordata/?data&data_type&node_id_include
                if 'data_type' in request.GET:
                    serializer = SensorDataSerializer_data_node_id_data_type(sensordata, many=True)

                # http://127.0.0.1:8000/sensordata/?data&node_id_include
                else:
                    serializer = SensorDataSerializer_data_node_id(sensordata, many=True)

            # http://127.0.0.1:8000/sensordata/?data&data_type
            elif 'data_type' in request.GET:
                serializer = SensorDataSerializer_data_data_type(sensordata, many=True)

            # http://127.0.0.1:8000/sensordata/?data
            else:
                serializer = SensorDataSerializer_data(sensordata, many=True)

        # http://127.0.0.1:8000/sensordata/?data_type
        elif 'data_type' in request.GET:
            serializer = SensorDataSerializer_data_type(sensordata, many=True)

        # http://127.0.0.1:8000/sensordata/?message_id
        elif 'message_id' in request.GET:
            serializer = SensorDataSerializer_message_id(sensordata, many=True)

        # http://127.0.0.1:8000/sensordata/?network
        elif 'network' in request.GET:
            serializer = SensorDataSerializer_network(sensordata, many=True)

        elif 'latitude' in request.GET:
            if 'node_id_include' in request.GET:
                # http://127.0.0.1:8000/sensordata/?latitude&longitude&node_id_include
                if 'longitude' in request.GET:
                    serializer = SensorDataSerializer_latitude_longitude_node_id(sensordata, many=True)

                # http://127.0.0.1:8000/sensordata/?latitude&node_id_include
                else:
                    serializer = SensorDataSerializer_latitude_node_id(sensordata, many=True)
            else:
                # http://127.0.0.1:8000/sensordata/?latitude
                serializer = SensorDataSerializer_latitude(sensordata, many=True)

        elif 'longitude' in request.GET:
            if 'node_id_include' in request.GET:
                # http://127.0.0.1:8000/sensordata/?latitude&longitude&node_id_include
                if 'latitude' in request.GET:
                    serializer = SensorDataSerializer_latitude_longitude_node_id(sensordata, many=True)

                # http://127.0.0.1:8000/sensordata/?longitude&node_id_include
                else:
                    serializer = SensorDataSerializer_longitude_node_id(sensordata, many=True)
            else:
                # http://127.0.0.1:8000/sensordata/?longitude
                serializer = SensorDataSerializer_longitude(sensordata, many=True)

        # http://127.0.0.1:8000/sensordata/?ram
        elif 'ram' in request.GET:
            serializer = SensorDataSerializer_ram(sensordata, many=True)

        # http://127.0.0.1:8000/sensordata/?received_at
        elif 'received_at' in request.GET:
            serializer = SensorDataSerializer_recieved_at(sensordata, many=True)

         # http://127.0.0.1:8000/sensordata/?record_id
        elif 'record_id' in request.GET:
            serializer = SensorDataSerializer_record_id(sensordata, many=True)

        elif 'timestamp' in request.GET:
            # http://127.0.0.1:8000/sensordata/?timestamp&node_id_include
            if 'node_id_include' in request.GET:
                serializer = SensorDataSerializer_timestamp_node_id(sensordata, many=True)

            # http://127.0.0.1:8000/sensordata/?timestamp
            else:
                serializer = SensorDataSerializer_timestamp(sensordata, many=True)

        # http://127.0.0.1:8000/sensordata/?version
        elif 'version' in request.GET:
            serializer = SensorDataSerializer_version(sensordata, many=True)

        # ********************************************
        # if no filtering or specific viewing requests
        # are made, serialize the entire data model
        # ********************************************

        # http://127.0.0.1:8000/sensordata/
        else:
            serializer = SensorDataSerializer(sensordata, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SensorDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def sensordata_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        sensordata = SensorData.objects.get(pk=pk)
    except SensorData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SensorDataSerializer(sensordata)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SensorDataSerializer(sensordata, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        sensordata.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SensorDataList(generics.ListAPIView):
    serializer_class = SensorDataSerializer
