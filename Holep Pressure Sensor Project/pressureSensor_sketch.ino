const float V_REF = 3.3;
const float R_BITS = 10.0;
const float MAX_ADC_READING = (1 << int(R_BITS)) - 1;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int raw_north = analogRead(A0);
  int raw_east = analogRead(A1);
  int raw_south = analogRead(A2);
  int raw_west = analogRead(A3);

  Serial.print((raw_north/MAX_ADC_READING)*V_REF); Serial.print(",");
  Serial.print((raw_east/MAX_ADC_READING)*V_REF); Serial.print(",");
  Serial.print((raw_south/MAX_ADC_READING)*V_REF); Serial.print(",");
  Serial.println((raw_west/MAX_ADC_READING)*V_REF);

  delay(50);
}
