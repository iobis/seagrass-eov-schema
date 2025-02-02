require 'json'

module Jekyll
  class DataPackageGenerator < Generator
    safe true
    priority :high

    def generate(site)
      file_path = File.join(site.source, '..', 'datapackage.json')
      if File.exist?(file_path)
        data = JSON.parse(File.read(file_path))
        site.data['datapackage'] = data
      end
      file_path = File.join(site.source, '..', 'seagrass-eov-profile.json')
      if File.exist?(file_path)
        data = JSON.parse(File.read(file_path))
        site.data['profile'] = data
      end
    end
  end
end