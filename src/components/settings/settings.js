let settings = {
  getURL: path => {
    let production = `http://${window.location.hostname}/api_blog/`;
    return production + path;
  }
};

export default settings;
