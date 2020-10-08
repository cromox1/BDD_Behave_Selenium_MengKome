Feature: Logging in with valid credentials

    Scenario: User login successfully

        Given I go to the site "mengkome.pythonanywhere.com"
        And I have a valid user
        When I type username
        And I type password
        And I click on 'Login'
        Then I should see the user information
        And I logout
        And I close the browser

    Scenario: User login successfully 2nd time

        Given I go to the site "mengkome.pythonanywhere.com"
        And I have a valid user
        When I type username
        And I type password
        And I click on 'Login'
        Then I should see the user information
        And I logout
        And I close the browser