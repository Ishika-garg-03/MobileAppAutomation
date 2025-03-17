Feature: Login Amazon

  @id:amazon_login
  Scenario: Go to Amazon and login
    Given Amazon application is installed on device
    When Try to login in amazon application
    Then User will be able to access amazon application