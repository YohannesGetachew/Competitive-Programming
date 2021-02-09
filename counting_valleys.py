def countingValleys(steps, path):
    if(steps >= 2 and steps <= pow(10, 6) and len(path) == steps):
        valleyCount = 0
        altitude = 0
        for count in range(0, steps):
            currentStep = path[count]
            if(currentStep == 'U'):
                altitude += 1
                if(altitude == 0):
                    valleyCount += 1
            elif(currentStep == 'D'):
                altitude -= 1
            else:
                continue
        return valleyCount
    else:
        print('Wrong arguments')


steps = 4
path = ['U', 'D',  'D', 'U']
Valleys = countingValleys(steps, path)
print(countingValleys(steps, path), "Valleys" if Valleys >
      1 or Valleys == 0 else "Valley")
