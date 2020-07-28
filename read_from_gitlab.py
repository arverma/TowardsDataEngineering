def read_yaml_from_gitlab():
    """
    Read any file content from Gitlab
    Gitlab File Path = path/to/file.yaml
    Gitlab Project_Id = 123
    :return: Resurce Yaml Content
    :rtype: dict
    """
    url = "https://<host>/api/v4/projects/{project_id}/repository/files/{f}/raw?ref=<branch>".format(
        project_id=<project_id>, f="path%2Fto%2Ffile%2Eyaml")
    resp = requests.get(url, headers={"Private-Token": "********************"})
    content_file = resp.content
    content_file.decode("utf-8")
    return yaml.safe_load(content_file)
