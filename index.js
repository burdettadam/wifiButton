#! /usr/bin/env node

var config = require('./config'),
    dash_button = require('node-dash-button'),
    dash = dash_button(config.button.id);
    request = require('request');

dash.on("detected", function (){
    sendToKRE(config.KRE.message);
    console.log("Ding");
  });

var sendToKRE = function(message){
  var url = config.KRE.webhook;
  request.post({url: url, json: message}, function(err, result){
    console.log('sent', message);
  });
};

