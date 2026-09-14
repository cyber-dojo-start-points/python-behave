
lambda { |stdout,stderr,status|
  output = stdout + stderr

  # A scenario whose assertion failed is red, and behave lists those.
  return :red if /Failing scenarios/.match(output)

  # Everything else is decided by behave's own scenario counts, which it
  # prints as "1 scenario passed, 0 failed, 0 skipped", adding an error
  # count when a step raised rather than failed. Reading the counts rather
  # than looking for "0 failed" is what keeps a run where nothing passed
  # from being called green.
  counts = /^(\d+) scenarios? passed, (\d+) failed(?:, (\d+) error)?/.match(output)
  return :amber if counts.nil?

  # A step that raised, or one behave has no definition for, is an error:
  # the run never got as far as finding out what the scenario would say.
  return :amber if counts[3].to_i != 0

  # Nothing passed, so there is nothing to be green about. This is an empty
  # feature file, a scenario that was skipped, and a feature file nothing
  # collected.
  return :amber if counts[1].to_i == 0

  return :green
}
