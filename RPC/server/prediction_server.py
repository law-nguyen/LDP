import grpc
import concurrent
from concurrent import futures

import prediction_pb2
import prediction_pb2_grpc

class PredictorServicer(prediction_pb2_grpc.PredictorServicer):
    
    def PredictAdhd(self, request):
        #call the class function that makes a prediction based on the request
        print(request)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    prediction_pb2_grpc.add_PredictorServicer_to_server(PredictorServicer(), server)
    print('Starting server. Listening on port 50051.')
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

serve()