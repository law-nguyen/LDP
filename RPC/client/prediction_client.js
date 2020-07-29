const grpc = require('grpc');
const messages = require('./prediction_pb');
const services = require('./prediction_grpc_pb');


function predict(data) {
  const answerData = [...data];
  const client = new services.PredictorClient(
    'localhost:50051', grpc.credentials.createInsecure()
  );
  const predictionRequest = new messages.PredictionRequest()
  
}

module.exports = {predict};
