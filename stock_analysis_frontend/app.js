var routerApp = angular.module('routerApp', ['ui.router','chart.js']);

routerApp.config(function($stateProvider, $urlRouterProvider) {
    
    $urlRouterProvider.otherwise('/home');
    
    $stateProvider
        .state('home', {
            url: '/home',
            templateUrl: 'partial-home.html',
            controller: 'scotchController'
        })
});

routerApp.service('DataService', [    
    '$q',
    '$http',
    function (
        $q,
        $http) {

        var self= this;

        self.getData = function (url) {
            var header = {
                'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'
            }
            var defer = $q.defer(),
                headerOptions = {
                    method: 'GET',
                    url: url,
                    headers : header,
                };
        
            $http(headerOptions).then(function (graphData) {
                defer.resolve(graphData.data);
            }, function (graphData) {
                defer.reject(graphData.data);
            });
            return defer.promise;
        }
}]);


routerApp.controller('scotchController', function($scope, DataService) {
    
    var url = "http://127.0.0.1:8000"+"/algo_task/get_stock_analysis/";
    DataService.getData(url).then(function (response) {
        $scope.tickerList = response;
    });


    $scope.fetchTickerData = function(){

        var url = "http://127.0.0.1:8000"+"/algo_task/get_stock_analysis/"+$scope.ticker+"/";
        DataService.getData(url).then(function (response) {
            if(response){
                if(response.lossgain_data){

                    var graphData = response.lossgain_data;
                    $scope.graphData = response.lossgain_data;

                    $scope.options = {
                        display : true
                    }

                    $scope.labels = ["Minusfiftyper", "Minustwentyfiveper", "Minusfifteenper", "Minustenper",
                     "Minuseightper", "Minussixper", "Minusfourper", "Minustwoper", "Twoper", "Fourper", "Sixper",
                     "Eightper", "Tenper", "Fifteenper", "Twentyfiveper", "Fiftyper"];

                    $scope.data = [graphData.minusfiftyper, graphData.minustwentyfiveper, graphData.minusfifteenper, graphData.minustenper,
                     graphData.minuseightper, graphData.minussixper, graphData.minusfourper, graphData.minustwoper, graphData.twoper, graphData.fourper, graphData.sixper,
                     graphData.eightper, graphData.tenper, graphData.fifteenper, graphData.twentyfiveper, graphData.fiftyper];
                }

                if(response.generalnumber_data){
                    $scope.otherData = response.generalnumber_data;
                }
            
            }
            
        });

    }
   
    
});