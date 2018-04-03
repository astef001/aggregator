var aggregator = angular.module('aggregator', ['djng.forms', 'ngCookies'], function($locationProvider){
  $locationProvider.html5Mode({enabled: true,
                              requireBase:false});
});

aggregator.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    var $cookies;
    angular.injector(['ngCookies']).invoke(['$cookies', function(_$cookies_) {
    $cookies = _$cookies_;
  }]);
}]);
