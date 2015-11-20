
var app = angular.module('main-app', []);

  app.controller('mainController', function($scope, $http){
      $scope.categorise = {};
      $scope.products = {};
      $scope.filterProduct = [];
      $scope.currentCategory;
      $scope.categorySelected = false;
      $scope.selectedProduct = {};
      $scope.quantity = 1;
      $scope.cart = [];
      $scope.cartClicked = false;
      $scope.thankyouPage = false;

      $scope.showCart = function() {
          $scope.cartClicked = true;
          console.log($scope.cartClicked)
      }

      $scope.hasValidQuantity = function() {
          n = $scope.quantity
          var floatN = parseFloat(n);
          return !isNaN(floatN) && isFinite(n) && floatN > 0 && floatN % 1 == 0;
      }

      $scope.placeOrder = function() {
          $http({
              url: '/place-order/', 
              method: "GET",
              params: {
                  first_name: $scope.fName,
                  last_name: $scope.lName,
                  email: $scope.email,
                  address: $scope.shippingAddress,
                  procucts: $scope.cart
              }
           }).then(function successCallback(response) {
              $scope.categorise = {};
              $scope.products = {};
              $scope.filterProduct = [];
              $scope.currentCategory = false;
              $scope.categorySelected = false;
              $scope.selectedProduct = {};
              $scope.quantity = 1;
              $scope.cart = [];
              $scope.cartClicked = false;
              $scope.thankyouPage = true;
          });
      }

      $scope.setCategory = function(categoryId){
          $scope.currentCategory = categoryId;
          $scope.filterProduct = [];
          $scope.cartClicked = false;
          $scope.thankyouPage = false;
          $http.get('/products/'+$scope.currentCategory).
            success(function(response) {
                $scope.products = response;
                if(response.length){
                    $scope.categorySelected = true;
                }
                else{
                    $scope.categorySelected = false;
                }
            }).
            error(function(response) {
               alert(response)
            });
      }

      $scope.setProduct = function(ProductId){
          $scope.selectedProduct = $scope.products.filter(function( obj ) {
              return obj.id == ProductId;
          });
          $scope.selectedProduct = $scope.selectedProduct[0]
      }

      $scope.addToCart = function(productId, quantity){
          product = $scope.products.filter(function( obj ) {
              return obj.id == productId;
          });
          product = product[0]
          product['quantity'] = quantity 
          $scope.cart.push(product)
          $scope.quantity = 1;
          console.log($scope.cart)
      }
 
      $scope.clearAllCart = function(){
          $scope.cart = [];
      }

      $scope.removeProductFromCart = function(product){
          for (var i =0; i < $scope.cart.length; i++) {
              if ($scope.cart[i].id == product.id) {
                  $scope.cart.splice(i,1);
                  break;
              }
          }
      }
 
      $http.get('/categorise').
          success(function(data, status, headers, config) {
              $scope.categories = data;
          }).
          error(function(data, status, headers, config) {
              alert(data)
          });

  }).config(function($interpolateProvider) {
      $interpolateProvider.startSymbol('[[');
      $interpolateProvider.endSymbol(']]');
  }).filter('keylength', function(){
      return function(input){
        if(!angular.isObject(input)){
            throw Error("Usage of non-objects with keylength filter!!")
        }
        return Object.keys(input).length;
     }
 });;
