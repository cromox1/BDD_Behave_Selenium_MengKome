Feature: Logging in with valid credentials

    Scenario: User login successfully

        Given I go to the site "mengkome.pythonanywhere.com"
        And I have a valid user
        When I type username
        When I type password
        When I click on 'Login'
        Then I should see the user information
        And I logout

    Scenario: User login successfully 2nd time

        Given I go to the site "mengkome.pythonanywhere.com"
        And I have a valid user
        When I type username
        When I type password
        When I click on 'Login'
        Then I should see the user information
        And I logout