<template>
    <canvas id='particles'></canvas>
</template>

<script>
import JQuery from 'jquery';
import Particle from '../js/particle';

const $ = JQuery;

export default {
  name: 'Particles',
  data() {
    return {
      particles: [],
      canvasElement: null,
      colors: [
        '#133046',
        '#15959F',
        '#F1E4B3',
        '#EC9770',
        '#C7402D',
      ],
      ctx: null,
      width: 0,
      height: 0,
      curry: 0,
      currx: 0,
    };
  },
  methods: {
    animate() {
      requestAnimationFrame(this.animate);
      this.ctx.beginPath();
      this.ctx.rect(0, 0, this.width, this.height);
      this.ctx.fillStyle = '#111';
      this.ctx.fill();
      for (let i = 0; i < this.particles.length; i += 1) {
        const particle = this.particles[i];
        particle.update(this.currx, this.curry, this.height, this.width);
        particle.draw(this.ctx);
      }
    },
    init(num) {
      this.particles = [];

      for (let x = 0; x < num; x += 1) {
        this.particles.push(new Particle(Math.random() * this.width, Math.random() * this.height,
          6, this.colors[Math.floor(Math.random() * this.colors.length)],
          Math.random() - 0.5, Math.random() - 0.5, Math.random() * 5));
      }

      this.particles.sort((a, b) => b.r - a.r);
    },
    createAnim() {
      $(document).ready(() => {
        this.canvasElement = document.getElementById('particles');

        this.canvasElement.width = window.innerWidth;
        this.canvasElement.height = window.innerHeight;
        this.canvasElement.style.padding = 0;
        this.ctx = this.canvasElement.getContext('2d');
        this.width = this.canvasElement.width;
        this.height = this.canvasElement.height;
        const num = Math.floor(this.width * this.height / 1920 / 1080 * 500);
        this.currx = -10000;
        this.curry = -10000;

        this.canvasElement.addEventListener('mousemove', (event) => {
          this.currx = event.clientX;
          this.curry = event.clientY;
        });

        this.canvasElement.addEventListener('touchstart', (event) => {
          this.currx = event.touches[0].clientX;
          this.curry = event.touches[0].clientY;
        });
        this.canvasElement.addEventListener('touchmove', (event) => {
          this.currx = event.touches[0].clientX;
          this.curry = event.touches[0].clientY;
        });
        this.canvasElement.addEventListener('touchend', () => {
          this.currx = -1000;
          this.curry = -1000;
        });

        this.init(num);

        this.animate();
      });
    },
    handleResize() {
      this.canvasElement.width = window.innerWidth;
      this.canvasElement.height = window.innerHeight;
      this.width = this.canvasElement.width;
      this.height = this.canvasElement.height;
      const num = Math.floor(this.width * this.height / 1920 / 1080 * 1000);
      this.init(num);
    },
  },
  created() {
    window.addEventListener('resize', this.handleResize);
    this.handleResize();
  },
  mounted() {
    this.createAnim();
  },
  destroyed() {
    window.removeEventListener('resize', this.handleResize);
  },

};
</script>

<style scoped>
#particles {
    height: 100%;
    width: 100%;
}
</style>
