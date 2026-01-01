const kavaText = `
var a[int] = 10;
var b[int] = 5;

print "Add: " + (a + b);
print "Sub: " + (a - b);
print "Mul: " + (a * b);
print "Div: " + (a / b);
`;

const jsText = `
public class Calculator {
    private static final double FIRST_NUMBER = 10;
    private static final double SECOND_NUMBER = 5;

    private static class CalculationResult {
        private String label;
        private double value;

        public CalculationResult(String label, double value) {
            this.label = label;
            this.value = value;
        }

        public String format() {
            return this.label + ": " + this.value;
        }
    }

    private static class ArithmeticProcessor {

        public CalculationResult performAddition(double a, double b) {
            double result = a + b;
            return new CalculationResult("Add", result);
        }

        public CalculationResult performSubtraction(double a, double b) {
            double result = a - b;
            return new CalculationResult("Sub", result);
        }

        public CalculationResult performMultiplication(double a, double b) {
            double result = a * b;
            return new CalculationResult("Mul", result);
        }

        public CalculationResult performDivision(double a, double b) {
            double result = a / b;
            return new CalculationResult("Div", result);
        }
    }

    public static void main(String[] args) {
        ArithmeticProcessor processorInstance = new ArithmeticProcessor();

        CalculationResult addition =
            processorInstance.performAddition(FIRST_NUMBER, SECOND_NUMBER);

        CalculationResult subtraction =
            processorInstance.performSubtraction(FIRST_NUMBER, SECOND_NUMBER);

        CalculationResult multiplication =
            processorInstance.performMultiplication(FIRST_NUMBER, SECOND_NUMBER);

        CalculationResult division =
            processorInstance.performDivision(FIRST_NUMBER, SECOND_NUMBER);

        System.out.println(addition.format());
        System.out.println(subtraction.format());
        System.out.println(multiplication.format());
        System.out.println(division.format());
    }
}
`;

const kavaEl = document.getElementById("kavaCode");
const jsEl = document.getElementById("jsCode");

let index = 0;

function type() {
  if (index <= kavaText.length || index <= jsText.length) {
    kavaEl.textContent = kavaText.slice(0, index);
    jsEl.textContent = jsText.slice(0, index);
    index++;
    setTimeout(type, 5);
  }
}

type();

/* Smooth scroll, i took this from other project of mine. */
(() => {
  const html = document.documentElement;

  let currentScroll = window.scrollY;
  let targetScroll = currentScroll;
  let isScrolling = false;
  const ease = 0.1;

  function smoothScroll() {
    currentScroll += (targetScroll - currentScroll) * ease;
    window.scrollTo(0, currentScroll);

    if (Math.abs(targetScroll - currentScroll) > 0.5) {
      requestAnimationFrame(smoothScroll);
    } else {
      isScrolling = false;
    }
  }

  window.addEventListener("wheel", e => {
    e.preventDefault();
    targetScroll += e.deltaY;
    targetScroll = Math.max(0, Math.min(targetScroll, html.scrollHeight - window.innerHeight));

    if (!isScrolling) {
      isScrolling = true;
      requestAnimationFrame(smoothScroll);
    }
  }, { passive: false });
})();
