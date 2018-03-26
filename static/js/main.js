var aggregator = angular.module('aggregator', ['djng.forms',]);
aggregator.controller('basicSearch', function($scope) {
	    $scope.basicSearchAction = function(){
	        $scope.test="dsadas"
	    console.log($scope.test)
	    }
    });
