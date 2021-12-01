import React from 'react';
import { List, Header } from 'semantic-ui-react';

export const Notes = ({ notes }) => {
    return (
        <List>
            {notes.map(note => {
                return (
                    <List.Item key={note.title}>
                        <Header>{note.title}</Header>
                        <List items={['NOTE: '+note.body, 'NOTE TYPE: '+note.type]} />
                    </List.Item>
                )
            })}
        </List>
    )   
}; 