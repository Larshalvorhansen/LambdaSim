;; Set up the NetLogo environment
globals []

turtles-own []

to setup
  clear-all
  create-turtles 10 ;; Creates 10 turtles
  ask turtles [
    setxy random-xcor random-ycor ;; Positions them randomly
  ]
  reset-ticks
end

to go
  ask turtles [
    right random 360
    forward 1
  ]
  tick
end
