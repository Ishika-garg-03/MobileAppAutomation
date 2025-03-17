Feature: Search and Install Amazon

  @id:install_app
  Scenario: Amazon Installation
    Given User is logged in on playstore
    When Try to search and install amazon application
    Then Amazon application should be installed