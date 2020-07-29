// GENERATED CODE -- DO NOT EDIT!

'use strict';
var grpc = require('grpc');
var prediction_pb = require('./prediction_pb.js');

function serialize_PredictionRequest(arg) {
  if (!(arg instanceof prediction_pb.PredictionRequest)) {
    throw new Error('Expected argument of type PredictionRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_PredictionRequest(buffer_arg) {
  return prediction_pb.PredictionRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_PredictionResponse(arg) {
  if (!(arg instanceof prediction_pb.PredictionResponse)) {
    throw new Error('Expected argument of type PredictionResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_PredictionResponse(buffer_arg) {
  return prediction_pb.PredictionResponse.deserializeBinary(new Uint8Array(buffer_arg));
}


var PredictorService = exports.PredictorService = {
  predict: {
    path: '/Predictor/Predict',
    requestStream: false,
    responseStream: false,
    requestType: prediction_pb.PredictionRequest,
    responseType: prediction_pb.PredictionResponse,
    requestSerialize: serialize_PredictionRequest,
    requestDeserialize: deserialize_PredictionRequest,
    responseSerialize: serialize_PredictionResponse,
    responseDeserialize: deserialize_PredictionResponse,
  },
};

exports.PredictorClient = grpc.makeGenericClientConstructor(PredictorService);
