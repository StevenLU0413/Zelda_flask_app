Feature: Zelda enemies information
  As player, one might want to know the information about specific enemies. My website can link player to the
  enemy they want to search for.




Scenario Outline: Get to know the information about Enemies
  Given the user is on the homepage
  When the user click on the link of <enemy_name>
  Then The information page about <this_enemy> should display

  Examples: Monsters
    |enemy_name             |  this_enemy         |
    |Silver Lynel           |Silver_Lynel         |
    |Gardian Skywatcher     |Gardian_Skywatcher   |
    |Black Moblin           |Black_Moblin         |


Scenario Outline: Users sees the image on the homepage
  Given the user is on the homepage
  When User want to know about this <enemy_id>
  Then The user should click the link under this <image_id> from the zelda api

  Examples: Monsters
  |enemy_id                  |image_id   |
  |123                       |123        |
  |126                       |126        |
  |110                       |110        |