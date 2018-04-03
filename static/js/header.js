aggregator.controller('HeaderController', function($scope, $location){
    $scope.isActive = function (viewLocation) {
        return viewLocation === $location.path();
    };
    
})


// function HeaderController($scope, $location) 
// { 
//     $scope.isActive = function (viewLocation) { 
//         return viewLocation === $location.path();
//     };
// }