import Setup
Setup. Create_screen()
Setup. press_loop()

while (Setup.health != 0):
    Setup. draw_compass()
    Setup. draw_health()
    Setup. Draw_player()
    Setup. draw_CannonCount()
    Setup. refresh_heading()
    Setup. t. clear()
