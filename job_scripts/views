import groovy.json.JsonSlurper

def viewFile = readFileFromWorkspace('views')
viewFile.eachLine(){ view ->
  def jsonSlurper = new JsonSlurper()
  def views = jsonSlurper.parseText(view)
  listView(views.name) {
    jobs{
      regex(views.jobs+/-.*/)
    }
    columns {
      status()
      weather()
      name()
      lastSuccess()
      lastFailure()
      lastDuration()
      buildButton()
    }
  }
}

