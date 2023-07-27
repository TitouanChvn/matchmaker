import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PlayerlistComponent } from './playerlist.component';

describe('PlayerlistComponent', () => {
  let component: PlayerlistComponent;
  let fixture: ComponentFixture<PlayerlistComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [PlayerlistComponent]
    });
    fixture = TestBed.createComponent(PlayerlistComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
