Feature: SourceDemo login
#    Scenario: Source Demo login
#      Given launch chrome browser
#      When open SourceDemo page
#      Then login
#      And close

#Scenario: Source Demo login
#      Given launch chrome browser
#      When login
#      Then close

#Scenario: Source Demo login
#      Given launch chrome browser
#      When login
#      Then navigate to left side
#Scenario: Source Demo login
#      Given launch chrome browser
#      When login
#      Then filter the product
#      Then close
#Scenario: Source Demo login
#      Given launch chrome browser
#      When login
#      Then select one product
#      Then add to cart
#      Then close

Scenario: Source Demo login
      Given launch chrome browser
      When login
      Then select one product
      Then add to cart
      Then go to cart iteam
      Then close

