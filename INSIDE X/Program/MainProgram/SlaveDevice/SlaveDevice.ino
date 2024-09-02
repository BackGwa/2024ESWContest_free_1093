#define STEP_SFR  80
#define STEP_IN1  5
#define STEP_IN2  6
#define STEP_IN3  7
#define STEP_IN4  8

#include <Stepper.h>

void move_cylinder(int sfr, int time);
Stepper cylinder(STEP_SFR, STEP_IN1, STEP_IN2, STEP_IN3, STEP_IN4);

void setup() {
  pinMode(0, INPUT_PULLUP);
  pinMode(1, INPUT_PULLUP);
  pinMode(2, INPUT_PULLUP);
  pinMode(3, INPUT_PULLUP);
  pinMode(4, INPUT_PULLUP);

  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);

  cylinder.setSpeed(300);
}

void loop() {
  // 신호 핀을 지정된 범위에서 지속적으로 검사
  for (int i = 0; i <= 3; i++) {
    if (digitalRead(i)) {
      digitalWrite(10 + i, HIGH);
    } else {
      digitalWrite(10 + i, LOW);
    }
  }

  if (digitalRead(4)) {
    move_cylinder(STEP_SFR, 250);
  }
}

/* 실린더 작동
 * 설정한 값과 시간만큼 실린더를 작동합니다. */
void move_cylinder(int sfr, int time) {
  cylinder.step(sfr);
  delay(time);
  cylinder.step(-sfr);
}