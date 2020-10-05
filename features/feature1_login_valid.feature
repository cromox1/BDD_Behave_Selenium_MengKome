Feature: Logging in with valid credentials

    Scenario: User login successfully

        Given I go to the site "mengkome.pythonanywhere.com"
        And I have a user
        When I type email
        When I type password
        When I click on 'Login'
        Then I should see the text Welcome