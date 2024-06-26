from datetime import date
import commands.settings


def saveGameDetailsOntoFile(gameDetails):
    if commands.settings.save:
        saveTime = date.today()
        saveFileName = str(gameDetails[0]) + ".txt"
        saveFileName = saveFileName.replace(":", "")
        print("Saved as: " + saveFileName)
        with open(saveFileName, 'a', encoding="utf-8") as f:
            gameTitle = gameDetails[0]
            productCode = gameDetails[1]
            gameReleaseDate = gameDetails[2]
            gamePlayers = gameDetails[3]
            gameLink = gameDetails[5]
            f.write(gameTitle + "\n")
            f.write(productCode + "\n")
            f.write(gameReleaseDate + "\n")
            f.write(gamePlayers + "\n")
            f.write(gameLink + "\n")
            f.write("Saved on this date: " + str(saveTime))
            f.close()
    else:
        print("This command is not enabled in settings")
