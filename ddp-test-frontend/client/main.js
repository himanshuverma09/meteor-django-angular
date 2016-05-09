import angular from 'angular';
import angularMeteor from 'angular-meteor';

angular.module('testing-ddp', [angularMeteor]);

angular.module('testing-ddp').controller("ddp-controller",['$scope',function($scope){
 $scope.himanshu ="Hello There"
  options = {};
  if (__meteor_runtime_config__.hasOwnProperty('DDP_DEFAULT_CONNECTION_URL')) {
    Django = Meteor;
  } else {
    Django = DDP.connect(window.location.protocol + '//'+window.location.hostname+':8000/');
    options.connection = Django;
  }
    Notification = new Mongo.Collection("django_ddp_app.notification", options);
    Notifications = Django.subscribe('Notifications');

    $scope.helpers({
      notification() {
        console.log(Notification.find({}).fetch());
        return Notification.find({}).fetch();
      }
    });


}]);
