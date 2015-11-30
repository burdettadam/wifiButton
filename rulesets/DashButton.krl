ruleset DashButton {
  meta {
    name "DashButton"
    description <<
      rulesets for 
      Amazon Dash Button events.
    >>
    author "Adam Burdett"
    logging on
  }
  global {

  }
  rule pressedButton{
    select when DashButton pressed_button
    pre {
      addr = event:attr("address").defaultsTo("no address passed","no address passed");
    }
    {
      noop();
    }
    always{
      log ("button pressed on #{addr}");
    }
  }
}