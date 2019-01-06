const MAX_RADIUS = 20;
const MAX_GRATE = 10;
const bounds = 100;
const VELDIV = Math.sqrt(2);

export default class Particle {
  constructor(x, y, r, c, vx, vy, vel) {
    this.x = x;
    this.y = y;
    this.c = c;
    this.r = MAX_RADIUS * (Math.sqrt((vx * vx + vy * vy) * vel) / VELDIV);
    this.vx = vx * vel;
    this.vy = vy * vel;
    this.grow = false;
    this.gRate = 1;
  }

  draw(ctx) {
    ctx.beginPath();
    if (this.grow) {
      ctx.arc(this.x, this.y, this.r * this.gRate, 0, 2 * Math.PI);
    } else {
      ctx.arc(this.x, this.y, this.r, 0, 2 * Math.PI);
    }
    ctx.fillStyle = this.c;
    ctx.fill();
  }

  update(currx, curry, height, width) {
    this.x += this.vx;
    this.y += this.vy;
    const val = ((currx - this.x) ** 2) + ((curry - this.y) ** 2);
    if (val < bounds * bounds) {
      this.grow = true;
      this.gRate = (MAX_GRATE - ((MAX_GRATE - 1) * val / bounds / bounds));
    } else {
      this.grow = false;
    }

    if (this.y < 0 || this.y > height) this.vy *= -1;
    if (this.x < 0 || this.x > width) this.vx *= -1;
  }
}
