import { forwardRef } from "react";

const Button = forwardRef(({ variant = "add", children, ...rest }, ref) => {
  return (
    <button className={`btn btn-${variant}`} ref={ref} {...rest}>
      {children}
    </button>
  );
});

export default Button;
