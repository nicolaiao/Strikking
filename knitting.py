import pyknit
print("Mønsteroppskrift: ")
row_measure_org = input("Pinnestørrelse: ")
if not row_measure_org == "":
  row_measure_org = float(row_measure_org)
  stitch_count_org = int(input("Antall masker per 10 cm: "))

  print("Garn / Testlapp: ")
  row_measure_yarn = 10*float(input("Pinnestørrelse: "))
  stitch_count_yarn = int(input("Antall masker per 10 cm: "))

  print("----------------")
  size = int(input("Hvor stort er det du skal strikke? [cm] "))

  pattern_recipe = pyknit.GaugeSwatch(
      stitch_count=stitch_count_org, stitch_measure=10, row_measure=row_measure_org, row_count=10, units='cm'
  )
  pattern_yarn = pyknit.GaugeSwatch(
      stitch_count=stitch_count_yarn, stitch_measure=10, row_measure=row_measure_yarn, row_count=10, units='cm'
  )

  size_out = pyknit.convert_stitch_measure(size, pattern_recipe, pattern_yarn)
  print(f"Hvis du strikker med samme pinner, men med ditt garn vil det bli {round(size_out, 1)} cm stort")

  delta_size = size - size_out
  changed_measurement = pattern_yarn.measurement_to_stitches(abs(delta_size))

  if delta_size > 0:
    print(f"Ønsker du å få samme størrelse må du strikke {changed_measurement} masker ekstra")
  else:
    print(f"Ønsker du å få samme størrelse må du strikke {changed_measurement} masker mindre")

start_count = int(input("Hvor mange masker har du i en omgang? "))
increase_number = int(input("Hvor mange masker skal du øke med? "))
recipe = pyknit.increase_evenly(
    starting_count=start_count,
    increase_number=increase_number, 
    in_the_round=True)

print(f"Følg denne oppskriften: {recipe}")
print(f"Tegnforklaring: \n k<tall> =strikk <tall> antall masker \n m<tall> = legg til <tall> antall masker")