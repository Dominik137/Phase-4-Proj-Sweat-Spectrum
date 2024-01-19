import { useState, useEffect } from "react";

function LogIn() {
  const [user, setUser] = useState(null);
  const [createUsername, setCreateUsername] = useState("");
  const [createPassword, setCreatePassword] = useState('');

  const [loginUsername, setLoginUsername] = useState("");
  const [loginPassword, setLoginPassword] = useState('');

  function handleSubmit(e) {
    e.preventDefault();
    if (loginUsername !== "") {
      fetch('/api/login', {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username: loginUsername,
          password: loginPassword
        })
      })
        .then(r => {
          if (r.ok) {
            return r.json();
          } else {
            return null;
          }
        })
        .then(data => setUser(data));
    // Clear form inputs after submission
    setLoginUsername("");
    setLoginPassword("");
    }
  }

  function handleCreateUser(e){
    e.preventDefault()
    console.log("Submitting user creation:", createUsername, createPassword);
    fetch('/api/create_user', {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username: createUsername,
        password: createPassword
      })
    })
      .then(r => {
        if (r.ok) {
          return r.json();
        } else {
          return null;
        }
      })
      .then(data => setUser(data));
      // Clear form inputs after submission
      setCreateUsername("");
      setCreatePassword("");
  }

  useEffect(() => {
    fetch('/api/session')
      .then(r => {
        if (r.ok) {
          return r.json();
        } else {
          return null;
        }
      })
      .then(data => setUser(data));
  }, []);

function handleLogout(id){
  fetch('/api/logout', {
  method: "DELETE"})
.then(r=>setUser(null))
}
// makes delete call to route logout which will perfrom the delete of user from session on backend 
// then it will setUser to null on the front end



  return (
    <>
      {user ?
        <>
          <h2>Welcome, {user.username}!</h2>
          <button onClick={handleLogout}>Logout</button>
        </>
        :
        <>
          <div>
              <h1>
                Create User!
              </h1>
              <form onSubmit={handleCreateUser}>
              <input
                type="text"
                value={createUsername}
                onChange={(e) => setCreateUsername(e.target.value)}
              />
              <input
                type="password"
                value={createPassword}
                onChange={(e) => setCreatePassword(e.target.value)}
              />
              <button type="submit">Create User</button>
            </form>
          </div>
          <br></br>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            value={loginUsername}
            onChange={(e) => setLoginUsername(e.target.value)}
          />
           <input
            type="password"
            value={loginPassword}
            onChange={(e) => setLoginPassword(e.target.value)}
          />
          <button type="submit">Login</button>
        </form>
        </>
      }
    </>
  );
}

export default LogIn;
